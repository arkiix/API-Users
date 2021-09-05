from config import *
import psycopg2


conn_string = f"host='{HOST}' dbname='{DATABASE}' user='{USER}' password='{PASSWORD}'"


def sql_execute(command):
    result = 'Done!'
    try:
        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor()
        cursor.execute(command)
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        result = error
    finally:
        if connection is not None:
            connection.close()

    return result


def sql_get(command):
    try:
        connection = psycopg2.connect(conn_string)
        cursor = connection.cursor()
        cursor.execute(command)
        result = cursor.fetchone()[0]
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        result = error
    finally:
        if connection is not None:
            connection.close()
    return result


def create_table():
    command = """
            CREATE TABLE IF NOT EXISTS public."Users"
            (
                "Id" integer NOT NULL GENERATED ALWAYS AS IDENTITY,
                "Name" character varying(50) NOT NULL,
                PRIMARY KEY ("Id")
            );"""
    return sql_execute(command)


def create_user(name):
    command = '''
            INSERT INTO "Users" ("Name")
            VALUES (\'%s\');''' % name
    sql_execute(command)
    command = '''
            SELECT "Id"
            FROM "Users"
            WHERE "Name" = \'%s\'''' % name
    return f'Done! Your id: {sql_get(command)}'


def delete_user(id):
    command = '''
            DELETE FROM "Users"
            WHERE "Id" = %d;''' % id
    return sql_execute(command)


def get_user(id):
    command = '''
            SELECT "Name"
            FROM "Users"
            WHERE "Id" = %d''' % id
    return sql_get(command)


def update_user(user):
    command = '''
            UPDATE "Users"
            SET "Name" = \'%s\'
            WHERE "Id" = %d''' % (user.name, user.id)
    return sql_execute(command)