CREATE TABLE IF NOT EXISTS cameras
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    name character(80),
    url character(2083),
    created_at timestamp(0) without time zone NOT NULL DEFAULT now(),
    CONSTRAINT cameras_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS filters
(
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    type character(80),
    camera_id uuid NOT NULL,
    created_at timestamp(0) without time zone NOT NULL DEFAULT now(),
    CONSTRAINT filters_pkey PRIMARY KEY (id),
    CONSTRAINT fk_filters_cameras
        FOREIGN KEY (camera_id)
        REFERENCES cameras (id)
        ON DELETE CASCADE
);
