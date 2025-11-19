import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    print("\n")
    print("*"*70)
    for row in cursor.fetchall():
        print(row)
    print("*" * 70)



def add_videos():
    name = input("enter the video name::")
    time = input("enter the video time::")
    cursor.execute("INSERT INTO videos(name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_videos():
    video_id = int(input("Enter Video ID to update:: "))
    name = input("enter the video name::")
    time = input("enter the video time::")
    print("Updated Successfully...")

    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()

def delete_videos():
    video_id = int(input("Enter Video ID to delete:: "))
    print("Successfully Deleted..")
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube Manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        choice = input("enter Your choice:: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                add_videos()
            case '3':
                update_videos()
            case '4':
                delete_videos()
            case '5':
                break
            case _:
                print("Invalid Option/Choice")

    conn.close()

if __name__ == "__main__":
    main()