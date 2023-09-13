from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import dotenv

DB_USERNAME = dotenv.get_key(".env", "DB_USERNAME")
DB_PASSWORD = dotenv.get_key(".env", "DB_PASSWORD")
DB_URL = dotenv.get_key(".env", "DB_URL")
DB_BUCKET = dotenv.get_key(".env", "DB_BUCKET")
DB_SCOPE = dotenv.get_key(".env", "DB_SCOPE")
print(DB_USERNAME, DB_PASSWORD, DB_URL, DB_BUCKET, DB_SCOPE)
username = DB_USERNAME
password = DB_PASSWORD
auth = PasswordAuthenticator(username, password)
cluster = Cluster.connect(
    "couchbases://{}".format(DB_URL),
    ClusterOptions(PasswordAuthenticator(username, password)),
)
bucket = cluster.bucket(DB_BUCKET)
scope = bucket.scope(DB_SCOPE)
collection = scope.collection("users")
scope.query("CREATE PRIMARY INDEX idx_email IF NOT EXISTS ON users USING GSI").execute()


def connectToDatabase():
    try:
        user = {
            "firstName": "Shreyash",
            "lastName": "Dhamane",
            "email": "shreyash.dhamane@gmail.com",
        }
        # result = cluster.query("SELECT `hello` AS greeting",QueryOptions(metric=True))
        collection.upsert("2", user)
        result = collection.get("2")
        # result =  cluster.query("SELECT firstName FROM `development`.sih.users LIMIT 10")
        print(result.value)

        # print(f"Report execution time: {result.metadata().metrics().execution_time()}")
    except CouchbaseException as ex:
        import traceback

        traceback.print_exc()
