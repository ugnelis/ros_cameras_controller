#!/usr/bin/env bash

MODE=${1:-"PRODUCTION"}
FORCE=${2:-false}
FRONT_END_DIR_PATH=../src/front_end_app
PUBLIC_DIR_PATH=../src/static

# If folder is empty and it is production mode.
if [ -z "$(ls ${PUBLIC_DIR_PATH})" ] && [ "${MODE}" == "PRODUCTION" ]; then
    FORCE=true
fi

# Install node modules if don't exist.
if [ ! -d "${FRONT_END_DIR_PATH}/node_modules" ]; then
    npm install --prefix ${FRONT_END_DIR_PATH}
fi

# Build front-end app.
if [ "${MODE}" == "PRODUCTION" ] && [ "${FORCE}" = true ]; then
    npm run --prefix ${FRONT_END_DIR_PATH} build
fi

# Run front-end app.
if [ "${MODE}" == "DEVELOPMENT" ]; then
    npm start --prefix ${FRONT_END_DIR_PATH}
fi
