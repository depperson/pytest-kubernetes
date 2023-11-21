from pytest_kubernetes.providers.base import AClusterManager
from pytest_kubernetes.options import ClusterOptions
from typing import Optional
from pathlib import PosixPath

class ExternalManager(AClusterManager):

    kubeconfig = PosixPath("~/.kube/config").expanduser()

    @classmethod
    def get_binary_name(self) -> str:
        return "echo"

    def _on_create(self, cluster_options: ClusterOptions, **kwargs) -> None:
        raise NotImplementedError

    def _on_delete(self) -> None:
        pass

    @property
    def kubeconfig(self) -> Optional[Path]:
        # TODO: make this configurable
        return PosixPath("~/.kube/config").expanduser()

    def load_image(self, image: str) -> None:
        raise NotImplementedError

    def delete(self) -> None:
        """Delete this cluster"""
        self._on_delete()
        # don't delete the kubeconfig file
