from db import test_connection
from queries import get_all_accounts

test_connection()
print(get_all_accounts())