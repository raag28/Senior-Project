""" from flask import Flask, request, render_template """
import scrapy

""" app = Flask(__name__) """

""" @app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        s_url = request.form.get("url")
        return "URL: " + s_url
    return render_template("popup.html") """


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [ 
        "https://youtube.com/"
    ]

    def parse(self, response):
        filename = 'page.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

""" if __name__ == '__main__':
    app.run() """

#    def parse(self, response):
#        for post in response.css('div.post-item'):
#            yield