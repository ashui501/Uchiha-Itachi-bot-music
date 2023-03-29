class pyUltroidError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
