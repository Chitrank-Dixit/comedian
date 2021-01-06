from click.testing import CliRunner
from sefct.sefct import checkCommand


class TestSideEffectArguments(object):
    def test_help_option(self):
        runner = CliRunner()
        result = runner.invoke(checkCommand, ["--help"])
        assert result.exit_code == 0
        assert (
            result.output
            == "Usage: checkcommand [OPTIONS] COMMAND\n\n  CLI tool used to run or dry run shell commands\n\nOptions:\n"
            "  -p, --platform TEXT  select shell platform Linux/OS X/Windows\n  -dr, --dry-run"
            "       dry run the command on shell\n  -c, --commit         run the command on shell\n  --help"
            "               Show this message and exit.\n"
        )

    def test_dry_run_option_no_command(self):
        runner = CliRunner()
        result = runner.invoke(checkCommand, ["--dry-run"])
        assert result.exit_code == 2
        assert (
            result.output
            == "Usage: checkcommand [OPTIONS] COMMAND\nTry 'checkcommand --help' for help.\n\nError: Missing argument "
            "'COMMAND'.\n"
        )

    def test_dry_run_option_with_command(self):
        runner = CliRunner()
        result = runner.invoke(checkCommand, ["--dry-run", "touch abc.txt"])
        assert result.exit_code == 0
        assert result.output == "dry run: True\ntouch abc.txt\n"

    def test_commit_option_no_command(self):
        runner = CliRunner()
        result = runner.invoke(checkCommand, ["--commit"])
        assert result.exit_code == 2
        assert (
            result.output
            == "Usage: checkcommand [OPTIONS] COMMAND\nTry 'checkcommand --help' for help.\n\nError: Missing argument "
            "'COMMAND'.\n"
        )

    def test_commit_option_with_command(self):
        runner = CliRunner()
        result = runner.invoke(checkCommand, ["--commit", "touch abc.txt"])
        assert result.exit_code == 0
        assert result.output == "commit: True\ntouch abc.txt\n"
