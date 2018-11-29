Schedule bot
====

## Development

Since we're cool and modern boys, we use docker for both dev & prod (for possible quick
scaling? :D). Local dev is simple: just run aiohttp service in docker with src
mounted.

``` shell
cp .env.example .env
make run
```

## Testing

[Pytest for
aiohttp](https://aiohttp.readthedocs.io/en/stable/testing.html#pytest-example),
run with:

``` shell
make test
```

Note what in testing environment postgres isn't mounted, so you need to
re-create models from scratch every time.

## Production

Production build is bit harder, we use caddy & certbot for easy ssl cert management:

``` shell

```


Possibly, webpack would be used for bundling js for admin dashboard to caddy's container.

## TODO:

Infrastructure tasks:
- [ ] Project description
- [X] local docker development
- [X] test structure
- [X] production configuration with nginx
- [ ] aiotg (polling)
- [x] Database initialization
- [x] Middleware
- [ ] db migrations
- [ ] db schema
- [ ] ci/cd
- [ ] rolling updates (zero downtime)
- [ ] Remove Dockerfile.testing

Coding tasks:
- [ ] aiotg (webhook for production)
- [ ] REA parser implementation
- [ ] vk & fb support
