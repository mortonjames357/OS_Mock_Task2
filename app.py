import os
import sqlite3
from flask import Flask, request, render_template
from setupDB import setup_DB, seed_DB


if __name__ == '__main__':
    setup_DB()
    seed_DB()

