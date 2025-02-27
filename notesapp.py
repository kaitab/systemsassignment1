#this is the module that will underly the notes API, etc.


class Note:
    def __init__(self, title : str, content : str):
        """initializes a note with a title and content"""
        self.title = title
        self.content = content

    def __str__(self):
        """returns a formatted string with the note's title and content"""
        return f"{self.title}: {self.content}"

    def get_title(self):
        """returns the note's title as a string"""
        return self.title

    def get_content(self):
        """returns the note's content as a string"""
        return self.content

class NotesApp:
    def __init__(self):
        """initializes the notes app, which is just a list that will contain notes"""
        self.list = []

    def list_all(self):
        """returns a list of all notes by title"""
        return self.list

    def add_note(self, title : str, content : str):
        """creates a new note with title and content, adds it to the list, and sends a message if its successfully added"""
        new_note = Note(title, content)
        self.list.append(new_note)
        if new_note in self.list:
            print("Note successfully added.")
            return "Note successfully added."
        else:
            print("Sorry, this note wasn't added.")
            return "Sorry, this note wasn't added."

    def return_note(self, title : str):
        """returns the content of a note given its title"""
        for note in self.list:
            if note.get_title() == title:
                print(note.get_content())
                return note.get_content()

    def search_notes(self, term):
        """returns a list of both the title and content of notes matching a search term"""
        found_list = []
        for note in self.list:
            title_list = note.get_title().split(" ")
            content_list = note.get_content().split(" ")
            if term in title_list or term in content_list:
                found_list.append(str(note))
        return found_list

