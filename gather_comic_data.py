""" Gather comic book data given a file that contains UPCs. """
import argparse
import csv
import time

from secrets import PUBLIC_KEY, PRIVATE_KEY

from marvel import Marvel

# Marvel API set-up
marvel = Marvel(PUBLIC_KEY, PRIVATE_KEY)
comics = marvel.comics

HEADERS = ['upc','title', 'authors', 'categories', 'tags', 'series', 'language', 'releaseDate',
           'pages', 'description', 'publisher', 'imageURL', 'thumbnailURL']

def get_upcs_from_file(args):
    """
    Gather UPCs from a file where each new line is a different UPC.

    It ignores lines that start with `#`.

    Returns:
        A list of processed UPCs.
    """
    UPCs = []
    # Gather UPCs from file
    with open(args.upcs_file, 'r', encoding='UTF8') as upcs_file:
        UPCs = [line.strip() for line in upcs_file if line and not line.startswith('#')]
    return UPCs

def get_upc_data(UPCs):
    """
    Obtain the comic book data via searching the marvel comic list for the specific UPC.

    If the UPC cannot be found, the UPC is noted in a list called `missing_upcs`.

    Returns:
        results: A list of processed comic book data.
        missing_upcs: A list of UPCs that were not found in the API and therefore not processed.
    """

    missing_upcs = []
    results = []

    print('Obtaining data...')
    for UPC in UPCs:
        if not UPC:
            continue

        print('UPC: %s' % UPC)

        # Look up the comic based on the UPC
        comic_search_response = comics.all(upc=UPC)

        # If there are no results to be found from the look-up, add the UPC to the missing_upcs list
        # and notify the user
        if not comic_search_response['data']['results']:
            missing_upcs.append(UPC)
            print('    FAIL')
            continue

        # Grab the first index since it should only return 1 result based on the single UPC
        comic_info = comic_search_response['data']['results'][0]

        results.append(clean_response(comic_info, UPC))
        print('    SUCCESS')

    return results, missing_upcs

def clean_response(comic_info, upc):
    """
    Clean comic book info into a digestible dictionary.

    Returns:
        A dictionary containing the cleaned info for a single comic book.
    """
    # Add together all the author names into one string
    author_string = ''
    for author in comic_info['creators']['items']:
        author_string += '%s, ' % author['name']

    # Combine image URLs into the full, proper URL string
    image_url = comic_info['images'][0]['path'] + '.' + comic_info['images'][0]['extension']
    thumbnail_url = comic_info['thumbnail']['path'] + '.' + comic_info['thumbnail']['extension']

    # Format the comic book info into just the data we need
    return {'upc': upc,
            'title': comic_info['title'],
            'authors': author_string,
            'categories': 'Comic Books',
            'tags': 'Star Wars',
            'series': comic_info['series']['name'],
            'language': 'English',
            'releaseDate': comic_info['dates'][0]['date'],
            'pages': comic_info['pageCount'],
            'description': comic_info['description'],
            'publisher': 'Marvel',
            'imageURL':image_url,
            'thumbnailURL': thumbnail_url
            }

def create_upc_data_csv(args, upc_data):
    """ Create a .csv containing cleaned comic book data and notifies the user. """
    if not upc_data:
        print('No data was retrieved. No import CSV to create.')
        return

    print('Creating import CSV...')
    # HEADERS = upc_data[0].keys()
    # Write completed CSV

    with open(f'{args.upcs_file.replace("upcs.txt", "")}csv.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.DictWriter(f, HEADERS)
        writer.writeheader()
        writer.writerows(upc_data)
    print('    Done!')

def create_missing_upc_file(missing_upcs):
    """ Create a .txt file containing upcs that could not be found by the Marvel API. """
    if missing_upcs:
        print('Creating missing UPCs txt file...')
        date = time.strftime('%m%d%Y-%H%M')
        with open(f'missing_upcs_{date}.txt', 'w', encoding='UTF8') as f:
            for missing_upc in missing_upcs:
                f.writelines(missing_upc)
                f.writelines('\n')
        print('    Done!')

def check_masterlist(UPCs):
    """ Check if the master list already has the given UPCs. If they do, it'll remove them from the list so they don't get unnecessarily processed. """
    print('Checking if UPCs have already been processed...')
    try:
        with open('comic_data_masterlist.csv', 'r', newline='', encoding='UTF-8') as f:
            pass
    except:
        with open('comic_data_masterlist.csv', 'w', newline='', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, HEADERS)
            writer.writeheader()
    finally:
        with open('comic_data_masterlist.csv', 'r', newline='', encoding='UTF-8') as f:
            master_info = f.read()

    UPCs = [UPC for UPC in UPCs if UPC not in master_info]
    print(f'    Found {len(UPCs)} UPCs to process...')
    print('')

    return UPCs

def append_masterlist(upc_data):
    """ Append found comic data to masterlist. """
    print('Updating comic data masterlist...')
    with open('comic_data_masterlist.csv', 'a', newline='', encoding='UTF-8') as f:
        dict_writer = csv.DictWriter(f, fieldnames=HEADERS)

        dict_writer.writerows(upc_data)
        print('    Done!')

def main():
    """ Main method. """
    # Instantiate the parser
    parser = argparse.ArgumentParser(
        description='This app gathers comic book data from Marvel UPC codes and creates a more \
                     easily digestible .csv file containing the comic book data.')

    # Required positional argument
    parser.add_argument('upcs_file',
                        help='.txt file containing UPCS codes separated on each line.')

    args = parser.parse_args()

    # Process the .txt file from the passed in path.
    UPCs = get_upcs_from_file(args)
    UPCs = check_masterlist(UPCs)
    # Gather the comic info.
    upc_data, missing_upcs = get_upc_data(UPCs)

    print()
    print('-' * 33)
    print()
    # Create the import csv.
    create_upc_data_csv(args, upc_data)
    append_masterlist(upc_data)
    # Create the missing UPC file.
    create_missing_upc_file(missing_upcs)


if __name__ == '__main__':
    main()
