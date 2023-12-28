# Search POC

This proof of concept (POC) is based on RediSearch and written in Python. Not much energy has been put into linting or
PEP-8, nor is the code optimized in any way. It's actually quite messy.

# Installation

After downloading the repository, simply run the following commands:

```commandline
> docker compose up --build --detach
> docker exec -it search-app python ingest.py
```

The `docker exec...` command is only required the first time building the service (or after running `docker compose
down`) hence can be left out.

# Usage

## API

When installed, the simple search API is available at `POST http://localhost/search`.

In order to perform a search include the query parameter `query`, example:

```
curl --location --request POST 'http://localhost:8800/search?query=the%20matrix'
```

Why POST when using query parameters? No particular reason. I guess I was thinking of using json payloads originally...
It's a POC, you'll live ;-)

The resulting response could be something like this
<details>
    <summary>Query: "the matrix"</summary>

````
{
    "movies": [
        {
            "_popularity": 81.263,
            "_score": 1.0,
            "adult": "0",
            "id": "movie:603",
            "original_title": "The Matrix",
            "payload": null,
            "popularity": "81.263",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 1.1915777777777778,
            "_score": 0.9555555555555556,
            "adult": "0",
            "id": "movie:509944",
            "original_title": "The Matwix",
            "payload": null,
            "popularity": "1.247",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 36.787882352941175,
            "_score": 0.9058823529411765,
            "adult": "0",
            "id": "movie:604",
            "original_title": "The Matrix Reloaded",
            "payload": null,
            "popularity": "40.61",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 6.4998000000000005,
            "_score": 0.9,
            "adult": "0",
            "id": "movie:14543",
            "original_title": "The Matrix Revisited",
            "payload": null,
            "popularity": "7.222",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 27.42802,
            "_score": 0.89,
            "adult": "0",
            "id": "movie:605",
            "original_title": "The Matrix Revolutions",
            "payload": null,
            "popularity": "30.818",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 3.0459714285714288,
            "_score": 0.8857142857142858,
            "adult": "0",
            "id": "movie:221495",
            "original_title": "The Matrix Recalibrated",
            "payload": null,
            "popularity": "3.439",
            "type": "movie",
            "video": "1"
        },
        {
            "_popularity": 62.559709090909095,
            "_score": 0.8818181818181818,
            "adult": "0",
            "id": "movie:624860",
            "original_title": "The Matrix Resurrections",
            "payload": null,
            "popularity": "70.944",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 2.32925,
            "_score": 0.875,
            "adult": "0",
            "id": "movie:684731",
            "original_title": "The Matrix Reloaded: Pre-Load",
            "payload": null,
            "popularity": "2.662",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 1.170224,
            "_score": 0.872,
            "adult": "0",
            "id": "movie:684428",
            "original_title": "The Matrix: What Is Bullet-Time?",
            "payload": null,
            "popularity": "1.342",
            "type": "movie",
            "video": "0"
        },
        {
            "_popularity": 1.680344,
            "_score": 0.872,
            "adult": "0",
            "id": "movie:684729",
            "original_title": "The Matrix Reloaded: Car Chase",
            "payload": null,
            "popularity": "1.927",
            "type": "movie",
            "video": "0"
        }
    ],
    "persons": [
        {
            "_popularity": 0.526984126984127,
            "_score": 0.8783068783068783,
            "adult": "0",
            "id": "person:2540910",
            "name": "Mattrix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.4955555555555556,
            "_score": 0.825925925925926,
            "adult": "0",
            "id": "person:2368741",
            "name": "John Matrix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.4828282828282829,
            "_score": 0.8047138047138048,
            "adult": "0",
            "id": "person:1351398",
            "name": "Jenny Matrix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.5502629629629631,
            "_score": 0.7783068783068784,
            "adult": "0",
            "id": "person:1283932",
            "name": "Jeff Hatrix",
            "payload": null,
            "popularity": "0.707",
            "type": "person"
        },
        {
            "_popularity": 0.45425685425685425,
            "_score": 0.757094757094757,
            "adult": "0",
            "id": "person:3875331",
            "name": "Mitch Mattix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.43333333333333335,
            "_score": 0.7222222222222222,
            "adult": "0",
            "id": "person:983872",
            "name": "Mike Marix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.4166666666666666,
            "_score": 0.6944444444444443,
            "adult": "0",
            "id": "person:2314977",
            "name": "Mihai Mitrix Mitrică",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.4150793650793651,
            "_score": 0.6917989417989419,
            "adult": "0",
            "id": "person:3455896",
            "name": "Mirose Patrix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 0.4061050061050061,
            "_score": 0.6768416768416768,
            "adult": "0",
            "id": "person:2850346",
            "name": "Lorenzo Mataix",
            "payload": null,
            "popularity": "0.6",
            "type": "person"
        },
        {
            "_popularity": 1.2787264957264957,
            "_score": 0.6680911680911681,
            "adult": "0",
            "id": "person:2799682",
            "name": "Maetrix Fitten",
            "payload": null,
            "popularity": "1.914",
            "type": "person"
        }
    ],
    "series": [
        {
            "_popularity": 15.447911111111111,
            "_score": 0.9037037037037037,
            "id": "series:711",
            "original_name": "Threat Matrix",
            "payload": null,
            "popularity": "17.094",
            "type": "series"
        },
        {
            "_popularity": 10.351666666666667,
            "_score": 0.8333333333333334,
            "id": "series:11393",
            "original_name": "Matrix",
            "payload": null,
            "popularity": "12.422",
            "type": "series"
        },
        {
            "_popularity": 0.545,
            "_score": 0.8333333333333334,
            "id": "series:31636",
            "original_name": "Matrix",
            "payload": null,
            "popularity": "0.654",
            "type": "series"
        },
        {
            "_popularity": 1.1801703703703703,
            "_score": 0.7925925925925926,
            "id": "series:116501",
            "original_name": "Escape The Matrix",
            "payload": null,
            "popularity": "1.489",
            "type": "series"
        },
        {
            "_popularity": 0.6311218855218856,
            "_score": 0.6033670033670034,
            "id": "series:220827",
            "original_name": "Rua da Matriz",
            "payload": null,
            "popularity": "1.046",
            "type": "series"
        },
        {
            "_popularity": 0.38526984126984126,
            "_score": 0.5873015873015873,
            "id": "series:38368",
            "original_name": "Approval Matrix",
            "payload": null,
            "popularity": "0.656",
            "type": "series"
        },
        {
            "_popularity": 0.4930718954248366,
            "_score": 0.586990351696234,
            "id": "series:68447",
            "original_name": "Matrix Chiambretti",
            "payload": null,
            "popularity": "0.84",
            "type": "series"
        },
        {
            "_popularity": 0.37241666666666656,
            "_score": 0.5694444444444443,
            "id": "series:18401",
            "original_name": "Paranormal Matrix",
            "payload": null,
            "popularity": "0.654",
            "type": "series"
        }
    ]
}
````
</details>


 ## ingest.py
```commandline
Usage: ingest.py [OPTIONS]

Options:
  --records / --no-records  ingest TMDb records
  --index / --no-index      create Redis searchable indexes
  --help                    Show this message and exit.
```
By default `ingest.py` will ingest the TMDb records and create Redis indexes. This should not harm anything, just
overwrite any keys that already exist. Error handling ensures that attempts to create indexes that already exist will be
handled somewhat gracefully.

# Please note

The import files included are exported from TMDb and are subject to their terms of use:
https://www.themoviedb.org/terms-of-use

The exports are in English only, so this POC generally only supports English searches for international titles. Local
titles should be available in the local language though, eg. searching for "adams æbler" or "Das Leben der Anderen" will
still return a valid results.
