"""

Making an object public
Sam is trying to decide how to upload a public CSV and share it with the world as Open Data.

She only wants to make that specific CSV public, and not the bucket.

She also doesn't want to make any of the other objects in the bucket public.

Help her decide the best way for her to do this.

Answer the question
50XP

        A presigned URL.  # access to a private object temporarily
 OK     A public-read ACL.
        A bucket policy.  # not  multi user environment.
        An IAM Policy.    # not  multi user environment.

"""
