import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Time, Boolean, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


DB_NAME = "sqlite3.db"
DB_DIALECT = "sqlite:///"
DB_DIR = os.getcwd() + "/db/"
ECHO = True

Base = declarative_base()


class Event:
    session_connect = "cowrie.session.connect"
    session_file_download = "cowrie.session.file_download"
    session_closed = "cowrie.session.closed"

    login_success = "cowrie.login.success"
    login_failed = "cowrie.login.failed"

    log_open = "cowrie.log.open"
    log_closed = "cowrie.log.closed"

    command_input = "cowrie.command.input"
    command_success = "cowrie.command.success"
    command_failed = "cowrie.command.failed"

    client_version = "cowrie.client.version"
    client_var = "cowrie.client.var"
    client_size = "cowrie.client.size"

    direct_tcpip_request = "cowrie.direct-tcpip.request"
    direct_tcpip_data = "cowrie.direct-tcpip.data"


class SessionConnect(Base):
    __tablename__ = "session_connects"

    id = Column(Integer, primary_key=True)
    protocol = Column(String)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    src_port = Column(Integer)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    dst_port = Column(Integer)
    dst_ip = Column(String)
    sensor = Column(String)


class LoginSuccess(Base):
    __tablename__ = "login_successes"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    password = Column(String)
    sensor = Column(String)


class LoginFailed(Base):
    __tablename__ = "login_fails"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    password = Column(String)
    sensor = Column(String)


class LogOpen(Base):
    __tablename__ = "log_opens"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    ttylog = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)


class CommandInput(Base):
    __tablename__ = "command_inputs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    input = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)


class CommandSuccess(Base):
    __tablename__ = "command_successes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    input = Column(Integer)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)


class CommandFailed(Base):
    __tablename__ = "command_fails"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    input = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)


class LogClosed(Base):
    __tablename__ = "log_closes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    ttylog = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)
    duration = Column(Float)
    size = Column(Integer)


class SessionClosed(Base):
    __tablename__ = "session_closes"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)
    duration = Column(Float)


class SessionFileDownload(Base):
    __tablename__ = "session_file_downloads"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)
    shasum = Column(String)
    outfile = Column(String)
    url = Column(String)
    realm = Column(String)


class ClientVersion(Base):
    __tablename__ = "client_versions"

    id = Column(Integer, primary_key=True)
    macCS = Column(String)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    kexAlgs = Column(String)
    keyAlgs = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    version = Column(String)
    compCS = Column(String)
    encCS = Column(String)
    sensor = Column(String)


class ClientVar(Base):
    __tablename__ = "client_vars"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)
    value = Column(String)


class DirectTCPIPRequest(Base):
    __tablename__ = "direct_tcpip_requests"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    src_port = Column(Integer)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    dst_port = Column(Integer)
    dst_ip = Column(String)
    sensor = Column(String)


class DirectTCPIPData(Base):
    __tablename__ = "direct_tcpip_datas"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    isError = Column(Boolean)
    src_ip = Column(String)
    dst_port = Column(Integer)
    dst_ip = Column(String)
    data = Column(String)
    sensor = Column(String)


class ClientSize(Base):
    __tablename__ = "client_size"

    id = Column(Integer, primary_key=True)
    timestamp = Column(String)
    session = Column(String)
    message = Column(String)
    system = Column(String)
    height = Column(Integer)
    width = Column(Integer)
    isError = Column(Boolean)
    src_ip = Column(String)
    sensor = Column(String)


class SrcIPLocation(Base):
    __tablename__ = "src_ip_locations"

    id = Column(Integer, primary_key=True)
    src_ip = Column(String)
    country_name = Column(String)
    country_iso = Column(String)
    state_name = Column(String)
    state_iso = Column(String)
    city_name = Column(String)
    zipcode = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


def create_db():

    if os.path.isfile(DB_DIR + DB_NAME):
        os.remove(DB_DIR + DB_NAME)

    engine = create_engine(DB_DIALECT + DB_DIR + DB_NAME, echo=ECHO)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    session.commit()


if __name__ == "__main__":
    create_db()
