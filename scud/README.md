
version = "0.2.3" --> Package Name changed from MSS to SCUP as pypi showed conflict. (SCUP as in SQL Covertor Utility Program)\n
version = "0.2.2" --> List command added and reponse to no query match added\n
version = "0.2.0" --> 3 Show commands working\n
version = "0.2.1" --> Patch - test scripts was commented out\n

7.1. Version numbering
Versioning is the process of adding unique identifiers to different versions of your package. The unique identifier you use may be name-based or number-based, but most Python packages use semantic versioning. In semantic versioning, a version number consists of three integers A.B.C, where A is the “major” version, B is the “minor” version, and C is the “patch” version. The first version of a software usually starts at 0.1.0 and increments from there. We call an increment a “bump”, and it consists of adding 1 to either the major, minor, or patch identifier as follows:

Patch release (0.1.0 -> 0.1.1): patch releases are typically used for bug fixes, which are backward compatible. Backward compatibility refers to the compatibility of your package with previous versions of itself. For example, if a user was using v0.1.0 of your package, they should be able to upgrade to v0.1.1 and have any code they previously wrote still work. It’s fine to have so many patch releases that you need to use two digits (e.g., 0.1.27).

Minor release (0.1.0 -> 0.2.0): a minor release typically includes larger bug fixes or new features that are backward compatible, for example, the addition of a new function. It’s fine to have so many minor releases that you need to use two digits (e.g., 0.13.0).

Major release (0.1.0 -> 1.0.0): release 1.0.0 is typically used for the first stable release of your package. After that, major releases are made for changes that are not backward compatible and may affect many users. Changes that are not backward compatible are called “breaking changes”. For example, changing the name of one of the modules in your package would be a breaking change; if users upgraded to your new package, any code they’d written using the old module name would no longer work, and they would have to change it.
