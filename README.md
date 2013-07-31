twitter-stream-vs-search
========================

Runs head to head a tweet search and a stream of tweets.


## Installing

```
$ sudo easy_install virtualenv
$ make install
```

## Running

Complete your app's twitter credentials in `settings.py` and run:

```
$ source venv/bin/activate
$ python run_test.py "keyword1,keyword2,.."
````

Hit `CTRL+C` to end the test and see results.
