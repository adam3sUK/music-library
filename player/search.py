def by_title_case_insensitive(query):
  return lambda track: query.lower() in track.title.lower()

def by_artist_case_insensitive(query):
  return lambda track: query.lower() in track.artist.lower()

def by_file_case_insensitive(query):
  return lambda track: query.lower() in track.file.lower()