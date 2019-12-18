# Vendors

Note that due to limitations in the Ruby build of SASS, it is not possible to `@include` plain `.css` files from vendor branches.

Instead, for convenience, we make symlinks to all the vendor css that we need, labelling the files `scss`, then we can `@include` them as normal.