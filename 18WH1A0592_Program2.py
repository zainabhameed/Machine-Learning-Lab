{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting db-sqlite3\n",
      "  Downloading db-sqlite3-0.0.1.tar.gz (1.4 kB)\n",
      "Collecting db\n",
      "  Downloading db-0.1.1.tar.gz (3.4 kB)\n",
      "Collecting antiorm\n",
      "  Downloading antiorm-1.2.1.tar.gz (171 kB)\n",
      "Building wheels for collected packages: db-sqlite3, db, antiorm\n",
      "  Building wheel for db-sqlite3 (setup.py): started\n",
      "  Building wheel for db-sqlite3 (setup.py): finished with status 'done'\n",
      "  Created wheel for db-sqlite3: filename=db_sqlite3-0.0.1-py3-none-any.whl size=1801 sha256=4b7ce92d8479d4684d3cfe48e6447908fb84be8b2ce4bc24405a869d29972554\n",
      "  Stored in directory: c:\\users\\fareed\\appdata\\local\\pip\\cache\\wheels\\9a\\a0\\6f\\b4ceab4614797b65af7a296172bf4bdc106702d7f18beafa57\n",
      "  Building wheel for db (setup.py): started\n",
      "  Building wheel for db (setup.py): finished with status 'done'\n",
      "  Created wheel for db: filename=db-0.1.1-py3-none-any.whl size=3899 sha256=2893854d8f7e10337eafb4b3c338e0493f0aa389f64e6ac09056a818635ffe4d\n",
      "  Stored in directory: c:\\users\\fareed\\appdata\\local\\pip\\cache\\wheels\\43\\94\\01\\2470e037a87c7f4fe93e4a110ee8c01b495d53db5de40b216b\n",
      "  Building wheel for antiorm (setup.py): started\n",
      "  Building wheel for antiorm (setup.py): finished with status 'done'\n",
      "  Created wheel for antiorm: filename=antiorm-1.2.1-py3-none-any.whl size=31670 sha256=d115467844e8574d0dab1c5b0f3a44e0fb54a77dceae79deae42c420a6edb7be\n",
      "  Stored in directory: c:\\users\\fareed\\appdata\\local\\pip\\cache\\wheels\\23\\fc\\3e\\c02e21af9692d533cae0374d54eb3502764cedb8a3edaf6e5c\n",
      "Successfully built db-sqlite3 db antiorm\n",
      "Installing collected packages: antiorm, db, db-sqlite3\n",
      "Successfully installed antiorm-1.2.1 db-0.1.1 db-sqlite3-0.0.1\n"
     ]
    }
   ],
   "source": [
    "!pip install db-sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "opened database successfully\n"
     ]
    }
   ],
   "source": [
    "conn=sqlite3.connect('exp2.db')\n",
    "cur=conn.cursor()\n",
    "conn=sqlite3.connect('test.db')\n",
    "print('opened database successfully');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Table created successfully\n"
     ]
    }
   ],
   "source": [
    "conn.execute('''CREATE TABLE COMPANY2\n",
    "            (ID INT PRIMARY KEY  NOT NULL,\n",
    "            NAME            TEXT NOT NULL,\n",
    "            AGE             INT  NOT NULL,\n",
    "            ADDRESS         CHAR(50),\n",
    "            SALARY          REAL);''')\n",
    "print(\"Table created successfully\");\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for row in conn.execute('select * from COMPANY2'):\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Records created successfully\n"
     ]
    }
   ],
   "source": [
    "\n",
    "conn.execute(\"INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)\\\n",
    "            VALUES (1, 'paul',32,'california',20000.00)\");\n",
    "conn.execute(\"INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)\\\n",
    "            VALUES (2, 'Alien',25,'Texas',30000.00 )\");\n",
    "conn.execute(\"INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)\\\n",
    "            VALUES (3, 'Teddy',23,'Norway',30000.00 )\");\n",
    "conn.execute(\"INSERT INTO COMPANY2 (ID,NAME,AGE,ADDRESS,SALARY)\\\n",
    "            VALUES (4, 'Mark',25,'Rich-Mond',15000.00 )\");\n",
    "conn.commit()\n",
    "print('Records created successfully');"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'paul', 32, 'california', 20000.0)\n",
      "(2, 'Alien', 25, 'Texas', 30000.0)\n",
      "(3, 'Teddy', 23, 'Norway', 30000.0)\n",
      "(4, 'Mark', 25, 'Rich-Mond', 15000.0)\n"
     ]
    }
   ],
   "source": [
    "for row in conn.execute('select * from COMPANY2'):\n",
    "    print(row)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
