from datetime import timedelta

from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, ClusterTimeoutOptions, QueryOptions
from dotenv import load_dotenv as load_d
import os

load_d()
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_BUCKET = os.getenv("DB_BUCKET")
DB_SCOPE = os.getenv("DB_SCOPE")
DB_PROTOCOL = os.getenv("DB_PROTOCOL")

auth = PasswordAuthenticator(DB_USERNAME, DB_PASSWORD)
cluster = Cluster.connect(
    "{}://{}".format(DB_PROTOCOL, DB_HOST),
    ClusterOptions(auth),
)
cb = cluster.bucket(DB_BUCKET)
scope = cb.scope(DB_SCOPE)

# scope.query("CREATE PRIMARY INDEX IF NOT EXISTS ON `development`.sih.users USING GSI").execute()

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
