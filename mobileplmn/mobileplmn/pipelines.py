# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from twisted.enterprise import adbapi


class MobileplmnPipeline:

    def __init__(self, mysql_config):
        self.db_con = adbapi.ConnectionPool(
            mysql_config["driver"],
            host=mysql_config["host"],
            db=mysql_config["db"],
            user=mysql_config["user"],
            passwd=mysql_config["password"],
            auth_plugin="mysql_native_password",
            charset="utf8",
        )

    def process_item(self, item, spider):
        result = self.db_con.runInteraction(self.insert_item, item)
        result.addErrback(self.handle_error)
        return item

    def insert_item(self, cursor, item):
        sql = "INSERT INTO plmns (MCC, MNC, ISO, Country, Country_Code, Network) VALUES (%s, %s, %s, %s, %s, %s)"
        args = (item["mcc"], item["mnc"], item["iso"], item["country"], item["country_code"], item["network"])
        cursor.execute(sql, args)

    def handle_error(self, e):
        print(e)

    @classmethod
    def from_crawler(cls, crawler):
        mysql_config = crawler.settings.get("MYSQL_DB_CONFIG")
        return cls(mysql_config)
