from datetime import timedelta

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, ClusterTimeoutOptions, QueryOptions
from dotenv import load_dotenv as load_d
import os

load_d()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_URL = os.getenv("DB_URL")
DB_BUCKET = os.getenv("DB_BUCKET")
DB_SCOPE = os.getenv("DB_SCOPE")


auth = PasswordAuthenticator(DB_USERNAME, DB_PASSWORD)
cluster = Cluster.connect(
    "couchbases://{}".format(DB_URL),
    ClusterOptions(auth),
)
# cluster.wait_until_ready(timedelta(seconds=5))
cb = cluster.bucket(DB_BUCKET)
scope = cb.scope(DB_SCOPE)


# # def connectToDatabase():
# #     try:
# #         user = {
# #             "firstName": "Shreyash",
# #             "lastName": "Dhamane",
# #             "email": "shreyash.dhamane@gmail.com",
# #         }
# #         # result = cluster.query("SELECT `hello` AS greeting",QueryOptions(metric=True))
# #         collection.upsert("2", user)
# #         result = collection.get("2")
# #         # result =  cluster.query("SELECT firstName FROM `development`.sih.users LIMIT 10")
# #         print(result.value)

# #         # print(f"Report execution time: {result.metadata().metrics().execution_time()}")
# #     except CouchbaseException as ex:
# #         import traceback

# #         traceback.print_exc()
