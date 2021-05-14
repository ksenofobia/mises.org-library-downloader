This little script downloads all free pdfs from Mises Institute library

You can make changes accordingly (i.e. increase number of pages if there's more now).
Also consider making a pull request.

Some changes can be made to tune it to your own preference.

For example in `link_pattern = re.compile(...)` you can add epub if you want that too/instead of pdfs.
Like this `(...)?(.pdf|.epub)` or just `(.epub)` instead.
