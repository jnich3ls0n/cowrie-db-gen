import os
import json
from declarative import SessionConnect, SessionClosed, SessionFileDownload
from declarative import LoginSuccess, LoginFailed
from declarative import LogOpen, LogClosed
from declarative import CommandInput, CommandSuccess, CommandFailed
from declarative import ClientVersion, ClientVar, ClientSize
from declarative import DirectTCPIPRequest, DirectTCPIPData
from declarative import SrcIPLocation
from declarative import Event
from declarative import DB_DIALECT, DB_DIR, DB_NAME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import geoip2.database


ECHO = False
JSON_DIR = os.getcwd() + "/json/"
LOCATION_DB = "GeoLite2-City.mmdb"


def get_event(event_json):
    e = event_json
    event_id = e['eventid']

    if event_id == Event.session_connect:
        return SessionConnect(protocol=e['protocol'],
                              timestamp=e['timestamp'],
                              session=e['session'],
                              message=e['message'],
                              src_port=e['src_port'],
                              system=e['system'],
                              isError=e['isError'],
                              src_ip=e['src_ip'],
                              dst_ip=e['dst_ip'],
                              sensor=e['sensor']
                              )

    if event_id == Event.login_success:
        return LoginSuccess(username=e['username'],
                            timestamp=e['timestamp'],
                            session=e['session'],
                            message=e['message'],
                            system=e['system'],
                            isError=e['isError'],
                            src_ip=e['src_ip'],
                            password=e['password'],
                            sensor=e['sensor']
                            )

    if event_id == Event.login_failed:
        return LoginFailed(username=e['username'],
                           timestamp=e['timestamp'],
                           session=e['session'],
                           message=e['message'],
                           system=e['system'],
                           isError=e['isError'],
                           src_ip=e['src_ip'],
                           password=e['password'],
                           sensor=e['sensor']
                           )

    if event_id == Event.log_open:
        return LogOpen(timestamp=e['timestamp'],
                       session=e['session'],
                       message=e['message'],
                       ttylog=e['ttylog'],
                       system=e['system'],
                       isError=e['isError'],
                       src_ip=e['src_ip'],
                       sensor=e['sensor']
                       )

    if event_id == Event.command_input:
        return CommandInput(timestamp=e['timestamp'],
                            session=e['session'],
                            message=e['message'],
                            system=e['system'],
                            isError=e['isError'],
                            src_ip=e['src_ip'],
                            input=e['input'],
                            sensor=e['sensor']
                            )

    if event_id == Event.command_success:
        return CommandSuccess(timestamp=e['timestamp'],
                              session=e['session'],
                              message=e['message'],
                              system=e['system'],
                              isError=e['isError'],
                              src_ip=e['src_ip'],
                              input=e['input'],
                              sensor=e['sensor']
                              )

    if event_id == Event.command_failed:
        return CommandFailed(timestamp=e['timestamp'],
                             session=e['session'],
                             message=e['message'],
                             system=e['system'],
                             isError=e['isError'],
                             src_ip=e['src_ip'],
                             input=e['input'],
                             sensor=e['sensor']
                             )

    if event_id == Event.log_closed:
        return LogClosed(timestamp=e['timestamp'],
                         session=e['session'],
                         message=e['message'],
                         ttylog=e['ttylog'],
                         system=e['system'],
                         isError=e['isError'],
                         src_ip=e['src_ip'],
                         sensor=e['sensor'],
                         duration=e['duration'],
                         size=e['size']
                         )

    if event_id == Event.session_closed:
        return SessionClosed(timestamp=e['timestamp'],
                             session=e['session'],
                             message=e['message'],
                             system=e['system'],
                             isError=e['isError'],
                             src_ip=e['src_ip'],
                             sensor=e['sensor'],
                             duration=e['duration']
                             )

    if event_id == Event.session_file_download:

        # (scp) realm: no shasum, outfile, or url

        if 'realm' in e.keys():
            return SessionFileDownload(timestamp=e['timestamp'],
                                       session=e['session'],
                                       message=e['message'],
                                       system=e['system'],
                                       isError=e['isError'],
                                       src_ip=e['src_ip'],
                                       sensor=e['sensor'],
                                       realm=e['realm']
                                       )

        else:
            return SessionFileDownload(timestamp=e['timestamp'],
                                       session=e['session'],
                                       message=e['message'],
                                       system=e['system'],
                                       isError=e['isError'],
                                       src_ip=e['src_ip'],
                                       sensor=e['sensor'],
                                       shasum=e['shasum'],
                                       outfile=e['outfile'],
                                       url=e['url']
                                       )

    if event_id == Event.client_version:
        macCS = ','.join(e['macCS'])
        keyAlgs = ','.join(e['keyAlgs'])
        kexAlgs = ','.join(e['kexAlgs'])
        compCS = ','.join(e['compCS'])
        encCS = ','.join(e['encCS'])

        return ClientVersion(macCS=macCS,
                             timestamp=e['timestamp'],
                             session=e['session'],
                             message=e['message'],
                             keyAlgs=keyAlgs,
                             kexAlgs=kexAlgs,
                             system=e['system'],
                             isError=e['isError'],
                             src_ip=e['src_ip'],
                             version=e['version'],
                             compCS=compCS,
                             encCS=encCS,
                             sensor=e['sensor']
                             )

    if event_id == Event.client_var:
        return ClientVar(name=e['name'],
                         timestamp=e['timestamp'],
                         session=e['session'],
                         message=e['message'],
                         system=e['system'],
                         isError=e['isError'],
                         src_ip=e['src_ip'],
                         sensor=e['sensor'],
                         value=e['value']
                         )

    if event_id == Event.direct_tcpip_request:
        return DirectTCPIPRequest(src_port=e['src_port'],
                                  timestamp=e['timestamp'],
                                  session=e['session'],
                                  message=e['message'],
                                  system=e['system'],
                                  isError=e['isError'],
                                  src_ip=e['src_ip'],
                                  dst_port=e['dst_port'],
                                  dst_ip=e['dst_ip'],
                                  sensor=e['sensor']
                                  )

    if event_id == Event.direct_tcpip_data:
        return DirectTCPIPData(timestamp=e['timestamp'],
                               session=e['session'],
                               message=e['message'],
                               system=e['system'],
                               isError=e['isError'],
                               src_ip=e['src_ip'],
                               dst_port=e['dst_port'],
                               dst_ip=e['dst_ip'],
                               data=e['data'],
                               sensor=e['sensor']
                               )

    if event_id == Event.client_size:
        return ClientSize(timestamp=e['timestamp'],
                          session=e['session'],
                          message=e['message'],
                          system=e['system'],
                          height=e['height'],
                          width=e['width'],
                          isError=e['isError'],
                          src_ip=e['src_ip'],
                          sensor=e['sensor'],
                          )


def populate_db():
    engine = create_engine(DB_DIALECT + DB_DIR + DB_NAME, echo=ECHO)
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Adding events to session...")

    ips = list()

    for file in os.listdir(JSON_DIR):
        if ".json" in file:
            with open(JSON_DIR + file, 'r') as f:
                for line_index, line in enumerate(f):
                    try:
                        json_obj = json.loads(line)

                        if 'src_ip' in json_obj.keys():
                            ips.append(json_obj['src_ip'])

                        event = get_event(json_obj)

                        if event:
                            session.add(event)
                        else:
                            print(file + ": " + str(line_index + 1) + ": Unknown Event: " + json_obj['eventid'])

                    except KeyError:
                        print("Key Error: " + line)
                        raise KeyError
                    except TypeError:
                        print("Type Error: " + line)
                        raise TypeError

    print("Done!")

    ip_set = set(ips)

    print("Adding Source IP Locations to session...")

    loc_reader = geoip2.database.Reader(DB_DIR + LOCATION_DB)

    for ip in ip_set:
        try:
            info = loc_reader.city(ip)
            src_ip_loc = SrcIPLocation(src_ip=ip,
                                       country_name=info.country.name,
                                       country_iso=info.country.iso_code,
                                       state_name=info.subdivisions.most_specific.name,
                                       state_iso=info.subdivisions.most_specific.iso_code,
                                       city_name=info.city.name,
                                       zipcode=info.postal.code,
                                       latitude=info.location.latitude,
                                       longitude=info.location.longitude
                                       )

            session.add(src_ip_loc)

        except geoip2.errors.AddressNotFoundError:
            print("Cannot find location data for " + ip)

    loc_reader.close()
    print("Done!")

    commit = input("Commit to {0}? [y/n]: ".format(DB_NAME))

    if commit == 'y':
        print('Committing changes...')
        session.commit()
        print("Finished!")
    else:
        pass


if __name__ == "__main__":
    populate_db()
