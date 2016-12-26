#   Question: 359. Logger Rate Limiter
# Difficulty: Easy
#       Tags: Hash Table, Design
'''
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if
and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given
timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

eg.
Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

'''


class Logger(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.logs = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message not in self.logs:
            self.logs[str(message)] = timestamp
            return True
        else:
            if timestamp - self.logs[message] < 10:
                return False
            else:
                self.logs[str(message)] = timestamp
                return True

logger = Logger()
# logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo"))

# logging string "bar" at timestamp 2
print(logger.shouldPrintMessage(2,"bar"))

# logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo"))

# logging string "bar" at timestamp 8
print(logger.shouldPrintMessage(8,"bar"))

# logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo"))

# logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo"))
