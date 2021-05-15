This little script downloads all free pdfs from Mises Institute library

You will need to install `urllib3` and `requests` modules from pip(`pip install urllib3 requests`), or in any other way you can find on the internet.

You can make changes accordingly (i.e. increase number of pages if there's more now).
Also consider making a pull request if that is the case.

Some changes can be made to tune it to your own preferences.

For example in `link_pattern = re.compile(...)` you can add epub if you want that too/instead of pdfs.
Like this `(...)?(.pdf|.epub)` or just `(.epub)` instead.
