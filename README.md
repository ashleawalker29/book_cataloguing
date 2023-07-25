# Book Cataloguing

---

## Marvel Python API
### Useful Links
[Marvel Python Package](https://pypi.org/project/marvel/)

[Official Documentation](https://developer.marvel.com/docs)

[Unofficial Documentation](https://speca.io/speca/marvel-public-api-v1#list-comics)

### Example API Response
``` json
{
"id": 96850,
"digitalId": 59169,
"title": "Star Wars: Han Solo & Chewbacca (2022) #2",
"issueNumber": 2,
"variantDescription": "",
"description": null,
"modified": "2022-07-09T09:08:32-0400",
"isbn": "",
"upc": "75960620225600211",
"diamondCode": "",
"ean": "",
"issn": "",
"format": "Comic",
"pageCount": 32,
"textObjects": [],
"resourceURI": "http://gateway.marvel.com/v1/public/comics/96850",
"urls": [
        {
            "type": "detail",
            "url": "http://marvel.com/comics/issue/96850/star_wars_han_solo_chewbacca_2022_2?utm_campaign=apiRef&utm_source=6a0a75d6dc26a7ead8d0effbf78667af"
        },
        {
            "type": "purchase",
            "url": "http://comicstore.marvel.com/Star-Wars-Han-Solo-Chewbacca-2/digital-comic/59169?utm_campaign=apiRef&utm_source=6a0a75d6dc26a7ead8d0effbf78667af"
        },
        {
            "type": "reader",
            "url": "http://marvel.com/digitalcomics/view.htm?iid=59169&utm_campaign=apiRef&utm_source=6a0a75d6dc26a7ead8d0effbf78667af"
        }
    ],
"series": {
        "resourceURI": "http://gateway.marvel.com/v1/public/series/33200",
        "name": "Star Wars: Han Solo & Chewbacca (2022 - 2023)"
    },
"variants": [
        {
            "resourceURI": "http://gateway.marvel.com/v1/public/comics/100895",
            "name": "Star Wars: Han Solo & Chewbacca (2022) #2 (Variant)"
        }
    ],
"collections": [],
"collectedIssues": [],
"dates": [
        {
            "type": "onsaleDate",
            "date": "2022-05-18T00:00:00-0400"
        },
        {
            "type": "focDate",
            "date": "2022-04-11T00:00:00-0400"
        },
        {
            "type": "unlimitedDate",
            "date": "2022-08-22T00:00:00-0400"
        },
        {
            "type": "digitalPurchaseDate",
            "date": "2022-03-29T00:00:00-0400"
        }
    ],
"prices": [
        {
            "type": "printPrice",
            "price": 3.99
        }
    ],
"thumbnail": {
        "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/50/62b9e2380fafb",
        "extension": "jpg"
    },
"images": [
        {
            "path": "http://i.annihil.us/u/prod/marvel/i/mg/c/50/62b9e2380fafb",
            "extension": "jpg"
        }
    ],
"creators": {
        "available": 6,
        "collectionURI": "http://gateway.marvel.com/v1/public/comics/96850/creators",
        "items": [
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/5251",
                    "name": "Vc Joe Caramagna",
                    "role": "letterer"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/644",
                    "name": "Marc Guggenheim",
                    "role": "writer"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/12120",
                    "name": "David Messina",
                    "role": "inker"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/13459",
                    "name": "Phil Noto",
                    "role": "penciler (cover)"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/4600",
                    "name": "Mark Paniccia",
                    "role": "editor"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/14265",
                    "name": "Alex Sinclair",
                    "role": "colorist"
                }
            ],
        "returned": 6
    },
"characters": {
        "available": 0,
        "collectionURI": "http://gateway.marvel.com/v1/public/comics/96850/characters",
        "items": [],
        "returned": 0
    },
"stories": {
        "available": 2,
        "collectionURI": "http://gateway.marvel.com/v1/public/comics/96850/stories",
        "items": [
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/stories/214768",
                    "name": "cover from Star Wars: Han Solo (2022) #2",
                    "type": "cover"
                },
                {
                    "resourceURI": "http://gateway.marvel.com/v1/public/stories/214769",
                    "name": "story from Star Wars: Han Solo (2022) #2",
                    "type": "interiorStory"
                }
            ],
        "returned": 2
     },
"events": {
        "available": 0,
        "collectionURI": "http://gateway.marvel.com/v1/public/comics/96850/events",
        "items": [],
        "returned": 0
    }
}

```
