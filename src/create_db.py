from db_setup import db

def main():
    try:
        db.create_all()
    except Exception as e:
        print(f"An error occurred creating the db: {e}")


if __name__ == '__main__':
    main()