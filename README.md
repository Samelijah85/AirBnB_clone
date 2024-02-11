# AirBnB Clone - Console

Welcome to the AirBnB clone project! This project marks the first stride toward constructing a full-fledged web application: the AirBnB clone. The primary objective of this endeavor is to develop a command-line interpreter that adeptly manages AirBnB objects like User, State, City, and Place. This command interpreter serves as the cornerstone for subsequent projects encompassing HTML/CSS templating, database storage, API, and front-end integration.

## Commands

The command interpreter facilitates interaction with and administration of AirBnB objects. It operates in interactive mode, furnishing a shell-like experience. The following commands are supported:

- **EOF**: Terminates the command interpreter.
- **quit**: Closes the program.
- **create <class>**: Generates a new instance of the specified class (e.g., BaseModel), stores it in the JSON file, and displays the **id**.
  + Example: `create BaseModel`
- **show <class> <id>**: Prints the string representation of an instance based on the class name and **id**.
  + Example: `show BaseModel 1234-1234-1234`
- **destroy <class> <id>**: Deletes an instance based on the class name and id, saving the alteration into the JSON file.
  + Example: `destroy BaseModel 1234-1234-1234`
- **all <class>**: Exhibits all string representations of instances based on the class name.
  + Example: `all BaseModel` or `all`
- **update <class> <id> <attribute> <value>**: Modifies an instance based on the class name and id by appending or revising attributes, saving the modification into the JSON file.
  + Example: `update BaseModel 1234-1234-1234 email "aibnb@mail.com"`

## How to Start

To commence the AirBnB clone command interpreter, execute the ensuing command in your terminal:

```bash
$ ./console.py
```

Upon executing this command, the following prompt will materialize:

```bash
(hbnb) 
```

This prompt signifies that you are in the "HBnB" console.

## How to Use

Once the command interpreter is operational, you can interact with it by entering commands. Utilize the `help` command to peruse the list of available commands along with their descriptions.

```bash
(hbnb) help
```

### Examples

```bash
$ ./console.py
(hbnb) create BaseModel
1234-1234-1234
(hbnb) show BaseModel 1234-1234-1234
[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323323), 'updated_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323326)}
(hbnb) update BaseModel 1234-1234-1234 first_name "person"
(hbnb) all BaseModel
["[BaseModel] (1234-1234-1234) {'id': '1234-1234-1234', 'created_at': datetime.datetime(2023, 11, 12, 13, 47, 18, 323323), 'updated_at': datetime.datetime(2023, 11, 12, 13, 48, 04, 919499), 'first_name': 'person'}"]
(hbnb) quit
$
```

Feel unrestricted to delve into and manage your AirBnB objects using the provided command interpreter!
