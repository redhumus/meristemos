#!/usr/bin/env python3
import musicbrainzngs
import sys

musicbrainzngs.set_useragent("python-musicbrainzngslookup", "0.1", "https://fossil.redhumus.org/fossil/meristemos")

def get_musicbrainz_metadata(acoustid_id):
    try:
        result = musicbrainzngs.get_metadata_by_acoustid(acoustid_id, includes=["artists", "recordings"])
    except musicbrainzngs.musicbrainz.ResponseError as error:
        print("Error al conectarse a MusicBrainz: %s" % error)
        sys.exit(1)
    except musicbrainzngs.musicbrainz.WebServiceError as error:
        print("Error en la respuesta de MusicBrainz: %s" % error)
        sys.exit(1)

    metadata = {}
    if "recording-list" in result:
        recordings = result["recording-list"]
        if len(recordings) > 0:
            recording = recordings[0]
            metadata["title"] = recording["title"]
            if "artist-credit" in recording:
                artists = recording["artist-credit"]
                if len(artists) > 0:
                    artist = artists[0]["artist"]
                    metadata["artist"] = artist["name"]
    return metadata
