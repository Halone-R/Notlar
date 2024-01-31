#!/bin/bash

# Run mongodump to create a backup
mongodump --uri="mongodb+srv://admin:admin23@notlar.bopwiue.mongodb.net/?retryWrites=true&w=majority" --gzip --out="src/data/backup"

