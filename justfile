#!/usr/bin/env just --justfile
#https://github.com/casey/just
set dotenv-load
set dotenv-filename := ".env.local"
default:
  just --list

nu := env_var('RUNNUEXE')

deploy:
    @{{nu}} scripts/deploy.nu