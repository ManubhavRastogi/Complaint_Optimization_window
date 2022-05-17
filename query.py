import sqlite3


# create a database or connect to one
conn = sqlite3.connect('Complaint_box.db')

            # create cursor
c = conn.cursor()


c.execute("DELETE FROM complaints WHERE complaintDate = '2022-05-17'")




# commit changes
conn.commit()

            # close connection
conn.close()