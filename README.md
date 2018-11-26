Schedule bot
====

## Development

Since we cool modern boys, we use docker for both dev & prod (for possible quick
scaling? :D). Local dev is simple: just run aiohttp service in docker with src
mounted.

``` shell
make run
```

## Testing

[Pytest for
aiohttp](https://aiohttp.readthedocs.io/en/stable/testing.html#pytest-example),
run with:

``` shell
make test
```

## Production

Production build is bit harder, we use caddy for easy ssl cert management:

``` shell

```

They communicate via socket, which is mounted to both containers. Database
configured separately.

This is minimal working example, supervisord may be added for ensuring what
docker services is always working.

Storing caddy config in open source git repo is ambiguous idea, but thing is:
nobody would never know server's location! Users communicate only with vk & tg &
fb, so we're safe.

Possibly, webpack would be used for bundling js for admin dashboard to caddy's container.

## TODO:

- [ ] Project description
- [X] local docker development
- [X] test structure
- [ ] production configuration with caddy
- [ ] aiotg (note what in production bots should work with webhook and with
      polling during local dev)
- [ ] Database initialization & middleware
- [ ] create aiohttp project template with vuejs
- [ ] db schema

- [ ] ci/cd
- [ ] REA parser implementation
- [ ] vk & fb support
