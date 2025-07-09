CREATE USER superset WITH PASSWORD 'superset';
CREATE DATABASE superset OWNER superset;
GRANT ALL PRIVILEGES ON DATABASE superset TO superset;

CREATE USER examples WITH PASSWORD 'examples';
CREATE DATABASE examples_db OWNER examples;
GRANT ALL PRIVILEGES ON DATABASE examples_db TO examples;
