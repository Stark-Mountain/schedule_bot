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

- [ ] Project description
- [X] local docker development
- [X] test structure
- [ ] production configuration with nginx
- [ ] aiotg (note what in production bots should work with webhook and with
      polling during local dev)
- [ ] Database initialization & middleware
- [ ] create aiohttp project template with vuejs
- [ ] db schema

- [ ] ci/cd
- [ ] REA parser implementation
- [ ] vk & fb support
