# geoDjango
<h2>A GeoDjango Example</h2>

<h3>Installation Steps</h3>
<ul>
 <li>
  <p>PostGIS</p>
  docker run --name some-postgis -p 25432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d mdillon/postgis
 </li>
 <li>
  <p>Database Connection</p>
  {
  'ENGINE': 'django.contrib.gis.db.backends.postgis',
  'NAME': 'postgres',
  'USER': 'postgres',
  'PASSWORD': 'mysecretpassword',
  'HOST': 'localhost',
  'PORT': 25432,
  }
 </li>
</ul>
