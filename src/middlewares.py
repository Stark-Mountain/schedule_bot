import time

from aiohttp.web import middleware


@middleware
async def perfomanceLoggingMiddleware(request, handler):
    """Just example"""
    ts = time.time()
    response = await handler(request)
    te = time.time()

    print("%r %2.2f ms" % (handler.__name__, (te - ts) * 1000))
    return response


middlewares = [perfomanceLoggingMiddleware]
