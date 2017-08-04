

class BotCMD:
    """
    abstraction class of a bot command. Create this for every command except very fundemental ones
    Override methods as necessary.
    """

    # execution activation command for when listening for mention commands
    command = None
    # set the argument vector for this command to execute based on runtime
    argv = None

    # defined error_code constants
    SUCCESS = 0             # success! you can execute this successfully.
    COMMAND_MISMATCH = -1   # not even the command matches.
    COMMAND_MATCH = 1       # in case the command matches, the error code is always positive! This isn't a success.
    INVALID_ARGV_FORMAT = -2# in case the argv is not a list of strings...



    def __init__(self, command:str, argv:list=None):
        self.command = command
        self.argv = argv

    def execute(self):
        """action of command"""
        pass

    def set_argv(self, argv:list):
        """set the argument vector of this command runtime"""
        self.argv = argv

    def isValid(self, command, argv=None):
        """
        determines whether the command can activate.
        This can be based on whether the given command matches the activation command,
        but it also can be based on argument vector checks and making sure that the arguments are valid.
        :param command; command thought to be the activation command
        :param argv: argument vector, contains command and extra arguments for the command
        :returns: 0 if successful, -1 if command doesn't match, or an error code indicating why it shouldn't activate.
        """
        if self.command == command:
            return self.COMMAND_MATCH
        else:
            return self.COMMAND_MISMATCH

    def get_error_msg(self, error_code:int):
        """
        this should be syncronized with the errorcodes returned by should_activate()
        it helps prompting the user why their input was wrong.
        :param errorcode: error code indicating why a certain command/argument vector are not valid input
        :returns: a specified message per every define error code, or None if none are found
        """
        error_msg = ""
        if error_code == self.COMMAND_MISMATCH:
            error_msg = "Command Mismatch"
        elif error_code == self.COMMAND_MATCH:
            error_msg = "Command Match"
        elif error_code == self.INVALID_ARGV_FORMAT:
            error_msg = "Invalid argv Format: must be a list of strings"
        else:
            error_msg = None
        return error_msg

    @staticmethod
    def get_help_format():
        """
         defines the help_format of this command. ex. "add <number> <number>". always contains command.
        :return: the format the command should be in
        """
        return "apply magic --on Target"

    @staticmethod
    def get_help_doc():
        """
        a little more detail into what a command does. This should be fairly basic. If sophisticated help is required,
        implement that separately.
        :return: documentation about the usage of a command
        """
        return "I'm just an abstract wand~ in an astract world~"