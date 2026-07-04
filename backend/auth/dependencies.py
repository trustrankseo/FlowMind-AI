from fastapi import Header, HTTPException


async def get_current_user(
    authorization: str | None = Header(default=None)
):

    if authorization is None:

        raise HTTPException(
            status_code=401,
            detail="Authentication Required"
        )

    return {
        "authenticated": True
    }