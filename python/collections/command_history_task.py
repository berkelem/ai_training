from collections import deque, namedtuple, Counter, ChainMap

Command = namedtuple('Command', ['command_str', 'timestamp', 'exit_status'])

class CommandHistory:
    
    def __init__(self, user_config=None):
        """
        user_config: dict with optional keys like 'max_history', 'max_failures'
        defaults: {'max_history': 100, 'max_failures': 10}
        """
        defaults = {'max_history': 100, 'max_failures': 10}
        self.config = ChainMap(user_config or {}, defaults)
        self.history = deque([], maxlen=self.config.get('max_history'))
        self.failures = deque([], maxlen=self.config.get('max_failures'))

    
    def add_command(self, command_str, timestamp, exit_status):
        c = Command(command_str=command_str, timestamp=timestamp, exit_status=exit_status)
        self.history.append(c)
        if exit_status != 0:
            self.failures.append(c)
    
    def get_most_used(self, n=5):
        """Return list of (command, count) for n most used commands"""
        count = Counter([s.command_str for s in self.history]).most_common(n)
        return count
    
    def get_recent_failures(self):
        """Return list of recent failed commands (up to max_failures)"""
        return list(self.failures)
    
    def get_config(self, key):
        """Get a config value (checks user config, then defaults)"""
        return self.config.get(key, None)


if __name__ == "__main__":
    history = CommandHistory({'max_history': 50})
    history.add_command('ls -la', '2026-01-13 10:00', 0)
    history.add_command('git status', '2026-01-13 10:01', 0)
    history.add_command('npm install', '2026-01-13 10:02', 1)  # failed
    history.add_command('ls -la', '2026-01-13 10:03', 0)

    print(history.get_most_used(3))  # [('ls -la', 2), ('git status', 1), ...]
    print(history.get_recent_failures())  # [Command(command='npm install', ...)]
    print(history.get_config('max_history'))  # 50