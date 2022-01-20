--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: bus_backend_bus; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_bus (
    id bigint NOT NULL,
    driver_id integer,
    entertainment boolean NOT NULL,
    extra_leg_room boolean NOT NULL,
    usb boolean NOT NULL,
    wifi boolean NOT NULL
);


ALTER TABLE public.bus_backend_bus OWNER TO postgres;

--
-- Name: bus_backend_bus_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_bus_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_bus_id_seq OWNER TO postgres;

--
-- Name: bus_backend_bus_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_bus_id_seq OWNED BY public.bus_backend_bus.id;


--
-- Name: bus_backend_route; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_route (
    id bigint NOT NULL,
    from_station_id bigint NOT NULL,
    to_station_id bigint NOT NULL
);


ALTER TABLE public.bus_backend_route OWNER TO postgres;

--
-- Name: bus_backend_route_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_route_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_route_id_seq OWNER TO postgres;

--
-- Name: bus_backend_route_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_route_id_seq OWNED BY public.bus_backend_route.id;


--
-- Name: bus_backend_seat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_seat (
    id bigint NOT NULL,
    sequence_number smallint NOT NULL,
    bus_id bigint NOT NULL,
    CONSTRAINT bus_backend_seat_sequence_number_check CHECK ((sequence_number >= 0))
);


ALTER TABLE public.bus_backend_seat OWNER TO postgres;

--
-- Name: bus_backend_seat_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_seat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_seat_id_seq OWNER TO postgres;

--
-- Name: bus_backend_seat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_seat_id_seq OWNED BY public.bus_backend_seat.id;


--
-- Name: bus_backend_station; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_station (
    id bigint NOT NULL,
    name character varying(255) NOT NULL,
    street_address character varying(255) NOT NULL,
    city character varying(28) NOT NULL
);


ALTER TABLE public.bus_backend_station OWNER TO postgres;

--
-- Name: bus_backend_station_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_station_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_station_id_seq OWNER TO postgres;

--
-- Name: bus_backend_station_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_station_id_seq OWNED BY public.bus_backend_station.id;


--
-- Name: bus_backend_ticket; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_ticket (
    id bigint NOT NULL,
    passenger_id integer NOT NULL,
    seat_id bigint NOT NULL,
    trip_id bigint NOT NULL
);


ALTER TABLE public.bus_backend_ticket OWNER TO postgres;

--
-- Name: bus_backend_ticket_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_ticket_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_ticket_id_seq OWNER TO postgres;

--
-- Name: bus_backend_ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_ticket_id_seq OWNED BY public.bus_backend_ticket.id;


--
-- Name: bus_backend_trip; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bus_backend_trip (
    id bigint NOT NULL,
    departure_time timestamp with time zone NOT NULL,
    bus_id bigint NOT NULL,
    route_id bigint NOT NULL
);


ALTER TABLE public.bus_backend_trip OWNER TO postgres;

--
-- Name: bus_backend_trip_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bus_backend_trip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bus_backend_trip_id_seq OWNER TO postgres;

--
-- Name: bus_backend_trip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bus_backend_trip_id_seq OWNED BY public.bus_backend_trip.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: bus_backend_bus id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_bus ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_bus_id_seq'::regclass);


--
-- Name: bus_backend_route id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_route ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_route_id_seq'::regclass);


--
-- Name: bus_backend_seat id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_seat ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_seat_id_seq'::regclass);


--
-- Name: bus_backend_station id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_station ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_station_id_seq'::regclass);


--
-- Name: bus_backend_ticket id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_ticket_id_seq'::regclass);


--
-- Name: bus_backend_trip id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_trip ALTER COLUMN id SET DEFAULT nextval('public.bus_backend_trip_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
3	Manager
1	Driver
2	Passenger
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	28
2	1	44
3	2	48
4	2	45
5	2	46
6	2	47
7	3	32
8	3	37
9	3	38
10	3	39
11	3	40
12	3	41
13	3	42
14	3	43
15	3	44
16	3	25
17	3	26
18	3	27
19	3	28
20	3	29
21	3	30
22	3	31
23	3	13
24	3	14
25	3	15
26	3	16
27	3	48
28	1	32
29	1	40
30	1	48
31	2	40
32	2	44
33	1	14
34	1	15
35	2	14
36	2	15
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add bus	7	add_bus
26	Can change bus	7	change_bus
27	Can delete bus	7	delete_bus
28	Can view bus	7	view_bus
29	Can add route	8	add_route
30	Can change route	8	change_route
31	Can delete route	8	delete_route
32	Can view route	8	view_route
33	Can add seat	9	add_seat
34	Can change seat	9	change_seat
35	Can delete seat	9	delete_seat
36	Can view seat	9	view_seat
37	Can add station	10	add_station
38	Can change station	10	change_station
39	Can delete station	10	delete_station
40	Can view station	10	view_station
41	Can add trip	11	add_trip
42	Can change trip	11	change_trip
43	Can delete trip	11	delete_trip
44	Can view trip	11	view_trip
45	Can add ticket	12	add_ticket
46	Can change ticket	12	change_ticket
47	Can delete ticket	12	delete_ticket
48	Can view ticket	12	view_ticket
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
7	pbkdf2_sha256$320000$VYbjQ5jXFDUNabM7ODvlGF$fGwyH4j4mCkJZDX9zf9m5mW/Y8OmPLlA736HCCzxQt4=	2022-01-15 00:21:20.269736-03	f	passenger_4	Test	Registration	test@registration.cl	f	t	2022-01-13 15:18:53.20844-03
18	pbkdf2_sha256$320000$WhAUCVjJrewBflyWrUVBri$iSGvsJ2f+5YC2zAayLuH75Wi1N6ceZPw5qZ1yX6RJIs=	2022-01-19 16:44:29.442932-03	f	mimi	Myrna	Araya	mimi@test.cl	f	t	2022-01-19 16:44:29.037184-03
5	sA*#48?^z6(2KJgs	2022-01-12 14:46:52.969844-03	f	passenger_3	Gustavo	Barrios Araya	gustavo.barrios@sansano.usm.cl	f	t	2022-01-12 14:46:27.786318-03
6	pbkdf2_sha256$320000$2Tm3btiXHvBfczvVuVSqCN$Q19RW2YSz1MjmFFMQi6ZaSBaXBhPw+PFnUTVMO+frRI=	2022-01-20 10:08:42.032574-03	f	manager				f	t	2022-01-13 14:46:42-03
23	pbkdf2_sha256$320000$55tr02PUI6p1akYlqfgo93$/l92UpeRtVOrSHNVQjWmASVqjbFmMVuFTJOjXFk5sgI=	2022-01-20 10:42:45.878531-03	f	sugatvo	Gustavo	Barrios	gustavo.barrios@test.cl	f	t	2022-01-20 05:10:31.641044-03
1	pbkdf2_sha256$320000$IpREm6jttMAFr984wFpRP7$OoGCPtJW3UvlKQcMekQhpzGMZk/OoNnZOcnX9XS56Zg=	2022-01-20 07:38:28.633191-03	t	admin			admin@example.com	t	t	2022-01-12 02:22:13.503878-03
13	pbkdf2_sha256$320000$jBCFjgDYJJQJFibqhD25nq$aRJn2sqqKwaUjjm7jioDpQl2do7om29SlMeIDK7MCPA=	2022-01-14 17:08:52.823879-03	f	driver_1	Driver	Test	driver@test.cl	f	t	2022-01-13 18:13:40.290602-03
24	pbkdf2_sha256$320000$GEkiHUURW9rw4YWaFOORyi$bHh6+VB6YBHd41SPgBo38aYVH+wDM1N2WtrDgCQXZ+Y=	\N	f	pedrito	Pedrito	Piedra	pedrito.piedra@test.cl	f	t	2022-01-20 08:07:38.661107-03
8	pbkdf2_sha256$320000$33Uje0l6sqgryPWIFog768$Nrc2af5ydVUMPrIyR8QE70mmGxSZidHpdVIWalA5+NI=	2022-01-18 18:03:47.435024-03	f	passenger_5	Test2	Registration	test2@registration.cl	f	t	2022-01-13 15:23:15.386082-03
14	pbkdf2_sha256$320000$TREcaoXZNHZSFdTGdFqjuH$sKO/W50vXwKFVEoyVA4IyowJeo7u4KmXvwXVzuu3GzI=	2022-01-14 17:26:37.742594-03	f	passenger_6				f	t	2022-01-14 17:25:56.097741-03
16	pbkdf2_sha256$320000$62y03pwWeHlCVx44uurznF$sDMHilwbv/p0WQuFOw3phiuGR8bpqYi+1aqkbDrThgM=	\N	f	nabeste	Esteban	Barrios	esteban.barrios@test.cl	f	t	2022-01-19 16:14:46.44759-03
17	pbkdf2_sha256$320000$pXTKKle922osAxMR3WovWB$2ff/KxXnA5ooCX0I+ggLw5KOA4siwe8BZcuSFU4X6os=	\N	f	camiloski	Camilo	Barrios	camilo.barrios@test.cl	f	t	2022-01-19 16:42:45.351288-03
26	pbkdf2_sha256$320000$0alP1T6dr1dqcm6EYCp6Rz$tw1UvvdMs/a5BJ2FGScThwfqcq11aIPMrHHRZpHiUmY=	\N	f	chofer_1	Chofer	Test	chofer@test.cl	f	t	2022-01-20 09:01:22.980796-03
27	pbkdf2_sha256$320000$1iyuJ4Qt84Mk8Iyu5ds0Yo$3/oTfIOCteCgkYAn+TFTs/qNnz/v1jC39e+y0dnJS+A=	\N	f	chofer_2	Choferini	Test	chofer@gtest.cl	f	t	2022-01-20 09:03:47.458757-03
28	pbkdf2_sha256$320000$hurCkoZcJm297vLhPrtWAm$uYWvT1oALfPBDzbbAOaA4WTg+8JgwIn+P6hox/9D5FY=	\N	f	chofer_3	Pedrito	Alameda	chofer_3@test.cl	f	t	2022-01-20 09:04:43.995702-03
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
3	5	2
4	6	3
5	7	2
6	8	2
9	13	1
10	14	2
12	16	2
13	17	2
14	18	2
19	23	2
20	24	1
22	26	1
23	27	1
24	28	1
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: bus_backend_bus; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_bus (id, driver_id, entertainment, extra_leg_room, usb, wifi) FROM stdin;
7	\N	t	t	t	t
8	\N	t	t	t	t
9	\N	f	f	f	f
\.


--
-- Data for Name: bus_backend_route; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_route (id, from_station_id, to_station_id) FROM stdin;
2	1	2
3	1	3
4	1	4
5	1	5
7	2	1
8	2	3
9	2	4
10	2	5
11	3	1
12	3	2
13	3	4
14	3	5
15	4	1
16	4	2
17	4	3
18	4	5
19	5	1
20	5	2
21	5	3
22	5	4
\.


--
-- Data for Name: bus_backend_seat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_seat (id, sequence_number, bus_id) FROM stdin;
52	1	7
53	2	7
54	3	7
55	4	7
56	5	7
57	6	7
58	7	7
59	8	7
60	9	7
61	10	7
62	1	8
63	2	8
64	3	8
65	4	8
66	5	8
67	6	8
68	7	8
69	8	8
70	9	8
71	10	8
72	1	9
73	2	9
74	3	9
75	4	9
76	5	9
77	6	9
78	7	9
79	8	9
80	9	9
81	10	9
\.


--
-- Data for Name: bus_backend_station; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_station (id, name, street_address, city) FROM stdin;
1	Terminal sur de Santiago	Av. Libertador Bernardo O'Higgins 3850	Santiago
2	Terminal Rodoviario de Calama	Granaderos 3048	Calama
3	Terminal de Coquimbo	Av. Varela 1300	Coquimbo
4	Terminal Rodoviario de Iquique	Patricio Lynch 50	Iquique
5	Terminal de Curicó	Prat 780	Curicó
\.


--
-- Data for Name: bus_backend_ticket; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_ticket (id, passenger_id, seat_id, trip_id) FROM stdin;
\.


--
-- Data for Name: bus_backend_trip; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bus_backend_trip (id, departure_time, bus_id, route_id) FROM stdin;
3	2022-01-16 05:00:00-03	7	2
4	2022-01-16 11:00:00-03	8	2
5	2022-01-17 17:30:00-03	9	2
6	2022-01-17 18:00:00-03	7	2
7	2022-01-17 19:00:00-03	8	2
8	2022-01-19 07:30:00-03	7	3
9	2022-01-19 08:30:00-03	8	3
10	2022-01-19 09:30:00-03	9	3
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-01-12 02:22:55.757677-03	1	Driver	1	[{"added": {}}]	3	1
2	2022-01-12 02:23:15.698066-03	2	Passenger	1	[{"added": {}}]	3	1
3	2022-01-12 02:24:17.336004-03	3	Manager	1	[{"added": {}}]	3	1
4	2022-01-12 02:26:24.9093-03	2	passenger_1	1	[{"added": {}}]	4	1
5	2022-01-12 02:26:40.527764-03	2	passenger_1	2	[{"changed": {"fields": ["Groups"]}}]	4	1
6	2022-01-12 02:27:10.338237-03	3	external_user_1	1	[{"added": {}}]	4	1
7	2022-01-12 12:38:42.062457-03	4	passanger_2	1	[{"added": {}}]	4	1
8	2022-01-12 12:38:53.590542-03	4	passanger_2	2	[{"changed": {"fields": ["Groups"]}}]	4	1
9	2022-01-12 13:17:04.670737-03	3	external_user_1	3		4	1
10	2022-01-13 14:46:43.058229-03	6	manager	1	[{"added": {}}]	4	1
11	2022-01-13 14:46:51.922285-03	6	manager	2	[{"changed": {"fields": ["Groups"]}}]	4	1
12	2022-01-13 18:09:43.650649-03	11	driver_1	3		4	1
13	2022-01-13 18:09:49.853691-03	12	driver_2	3		4	1
14	2022-01-14 15:40:12.529038-03	3	Manager	2	[{"changed": {"fields": ["Permissions"]}}]	3	1
15	2022-01-14 15:41:16.777953-03	1	Driver	2	[{"changed": {"fields": ["Permissions"]}}]	3	1
16	2022-01-14 15:41:35.72108-03	2	Passenger	2	[{"changed": {"fields": ["Permissions"]}}]	3	1
17	2022-01-14 15:41:48.575973-03	2	Passenger	2	[]	3	1
18	2022-01-14 16:31:45.837769-03	1	Driver	2	[{"changed": {"fields": ["Permissions"]}}]	3	1
19	2022-01-14 16:31:52.671968-03	2	Passenger	2	[{"changed": {"fields": ["Permissions"]}}]	3	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	bus_backend	bus
8	bus_backend	route
9	bus_backend	seat
10	bus_backend	station
11	bus_backend	trip
12	bus_backend	ticket
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-01-11 17:50:20.353244-03
2	auth	0001_initial	2022-01-11 17:50:20.437696-03
3	admin	0001_initial	2022-01-11 17:50:20.457893-03
4	admin	0002_logentry_remove_auto_add	2022-01-11 17:50:20.46391-03
5	admin	0003_logentry_add_action_flag_choices	2022-01-11 17:50:20.470374-03
6	contenttypes	0002_remove_content_type_name	2022-01-11 17:50:20.485726-03
7	auth	0002_alter_permission_name_max_length	2022-01-11 17:50:20.493707-03
8	auth	0003_alter_user_email_max_length	2022-01-11 17:50:20.501704-03
9	auth	0004_alter_user_username_opts	2022-01-11 17:50:20.508703-03
10	auth	0005_alter_user_last_login_null	2022-01-11 17:50:20.515649-03
11	auth	0006_require_contenttypes_0002	2022-01-11 17:50:20.517642-03
12	auth	0007_alter_validators_add_error_messages	2022-01-11 17:50:20.524625-03
13	auth	0008_alter_user_username_max_length	2022-01-11 17:50:20.537308-03
14	auth	0009_alter_user_last_name_max_length	2022-01-11 17:50:20.545325-03
15	auth	0010_alter_group_name_max_length	2022-01-11 17:50:20.553268-03
16	auth	0011_update_proxy_permissions	2022-01-11 17:50:20.562244-03
17	auth	0012_alter_user_first_name_max_length	2022-01-11 17:50:20.57025-03
18	bus_backend	0001_initial	2022-01-11 17:50:20.675732-03
19	sessions	0001_initial	2022-01-11 17:50:20.687732-03
20	bus_backend	0002_bus_manufacturer_bus_type_alter_bus_driver	2022-01-11 18:39:33.176023-03
21	bus_backend	0003_alter_ticket_unique_together	2022-01-12 11:25:03.67945-03
22	bus_backend	0004_alter_ticket_passenger	2022-01-12 13:15:38.027185-03
23	bus_backend	0005_alter_seat_bus	2022-01-13 17:28:38.771021-03
24	bus_backend	0006_alter_bus_driver	2022-01-13 17:58:10.708947-03
25	bus_backend	0007_alter_bus_driver	2022-01-13 18:09:02.216718-03
26	bus_backend	0008_alter_bus_driver	2022-01-13 18:16:24.265055-03
27	bus_backend	0007_remove_bus_manufacturer_remove_bus_type	2022-01-16 12:32:00.031966-03
28	bus_backend	0008_bus_entertainment_bus_extra_leg_room_bus_usb_and_more	2022-01-16 13:09:36.146928-03
29	bus_backend	0009_alter_route_unique_together	2022-01-17 14:35:22.395602-03
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 36, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 48, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 25, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 29, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: bus_backend_bus_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_bus_id_seq', 9, true);


--
-- Name: bus_backend_route_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_route_id_seq', 22, true);


--
-- Name: bus_backend_seat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_seat_id_seq', 81, true);


--
-- Name: bus_backend_station_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_station_id_seq', 5, true);


--
-- Name: bus_backend_ticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_ticket_id_seq', 12, true);


--
-- Name: bus_backend_trip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bus_backend_trip_id_seq', 10, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 19, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 12, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 29, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: bus_backend_bus bus_backend_bus_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_bus
    ADD CONSTRAINT bus_backend_bus_pkey PRIMARY KEY (id);


--
-- Name: bus_backend_route bus_backend_route_from_station_id_to_station_id_b3f83390_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_route
    ADD CONSTRAINT bus_backend_route_from_station_id_to_station_id_b3f83390_uniq UNIQUE (from_station_id, to_station_id);


--
-- Name: bus_backend_route bus_backend_route_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_route
    ADD CONSTRAINT bus_backend_route_pkey PRIMARY KEY (id);


--
-- Name: bus_backend_seat bus_backend_seat_bus_id_sequence_number_a49c3fca_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_seat
    ADD CONSTRAINT bus_backend_seat_bus_id_sequence_number_a49c3fca_uniq UNIQUE (bus_id, sequence_number);


--
-- Name: bus_backend_seat bus_backend_seat_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_seat
    ADD CONSTRAINT bus_backend_seat_pkey PRIMARY KEY (id);


--
-- Name: bus_backend_station bus_backend_station_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_station
    ADD CONSTRAINT bus_backend_station_pkey PRIMARY KEY (id);


--
-- Name: bus_backend_ticket bus_backend_ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket
    ADD CONSTRAINT bus_backend_ticket_pkey PRIMARY KEY (id);


--
-- Name: bus_backend_ticket bus_backend_ticket_trip_id_seat_id_d28ed7f8_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket
    ADD CONSTRAINT bus_backend_ticket_trip_id_seat_id_d28ed7f8_uniq UNIQUE (trip_id, seat_id);


--
-- Name: bus_backend_trip bus_backend_trip_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_trip
    ADD CONSTRAINT bus_backend_trip_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: bus_backend_bus_driver_id_eaab4931; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_bus_driver_id_eaab4931 ON public.bus_backend_bus USING btree (driver_id);


--
-- Name: bus_backend_route_from_station_id_3b29a4f3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_route_from_station_id_3b29a4f3 ON public.bus_backend_route USING btree (from_station_id);


--
-- Name: bus_backend_route_to_station_id_e3cce74c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_route_to_station_id_e3cce74c ON public.bus_backend_route USING btree (to_station_id);


--
-- Name: bus_backend_seat_bus_id_0048db19; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_seat_bus_id_0048db19 ON public.bus_backend_seat USING btree (bus_id);


--
-- Name: bus_backend_ticket_passenger_id_4c826f72; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_ticket_passenger_id_4c826f72 ON public.bus_backend_ticket USING btree (passenger_id);


--
-- Name: bus_backend_ticket_seat_id_0b34db4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_ticket_seat_id_0b34db4b ON public.bus_backend_ticket USING btree (seat_id);


--
-- Name: bus_backend_ticket_trip_id_b76145f1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_ticket_trip_id_b76145f1 ON public.bus_backend_ticket USING btree (trip_id);


--
-- Name: bus_backend_trip_bus_id_235b88df; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_trip_bus_id_235b88df ON public.bus_backend_trip USING btree (bus_id);


--
-- Name: bus_backend_trip_route_id_61577b92; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX bus_backend_trip_route_id_61577b92 ON public.bus_backend_trip USING btree (route_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_bus bus_backend_bus_driver_id_eaab4931_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_bus
    ADD CONSTRAINT bus_backend_bus_driver_id_eaab4931_fk_auth_user_id FOREIGN KEY (driver_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_route bus_backend_route_from_station_id_3b29a4f3_fk_bus_backe; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_route
    ADD CONSTRAINT bus_backend_route_from_station_id_3b29a4f3_fk_bus_backe FOREIGN KEY (from_station_id) REFERENCES public.bus_backend_station(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_route bus_backend_route_to_station_id_e3cce74c_fk_bus_backe; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_route
    ADD CONSTRAINT bus_backend_route_to_station_id_e3cce74c_fk_bus_backe FOREIGN KEY (to_station_id) REFERENCES public.bus_backend_station(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_seat bus_backend_seat_bus_id_0048db19_fk_bus_backend_bus_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_seat
    ADD CONSTRAINT bus_backend_seat_bus_id_0048db19_fk_bus_backend_bus_id FOREIGN KEY (bus_id) REFERENCES public.bus_backend_bus(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_ticket bus_backend_ticket_passenger_id_4c826f72_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket
    ADD CONSTRAINT bus_backend_ticket_passenger_id_4c826f72_fk_auth_user_id FOREIGN KEY (passenger_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_ticket bus_backend_ticket_seat_id_0b34db4b_fk_bus_backend_seat_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket
    ADD CONSTRAINT bus_backend_ticket_seat_id_0b34db4b_fk_bus_backend_seat_id FOREIGN KEY (seat_id) REFERENCES public.bus_backend_seat(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_ticket bus_backend_ticket_trip_id_b76145f1_fk_bus_backend_trip_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_ticket
    ADD CONSTRAINT bus_backend_ticket_trip_id_b76145f1_fk_bus_backend_trip_id FOREIGN KEY (trip_id) REFERENCES public.bus_backend_trip(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_trip bus_backend_trip_bus_id_235b88df_fk_bus_backend_bus_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_trip
    ADD CONSTRAINT bus_backend_trip_bus_id_235b88df_fk_bus_backend_bus_id FOREIGN KEY (bus_id) REFERENCES public.bus_backend_bus(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: bus_backend_trip bus_backend_trip_route_id_61577b92_fk_bus_backend_route_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bus_backend_trip
    ADD CONSTRAINT bus_backend_trip_route_id_61577b92_fk_bus_backend_route_id FOREIGN KEY (route_id) REFERENCES public.bus_backend_route(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

