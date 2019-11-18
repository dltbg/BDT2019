# Implementasi MongoDB

## Spesifikasi Server
### Seluruh Server Menggunakan
  - OS    : Ubuntu 18.04
  - RAM   : 512 MB
### IP tiap Server
  - Mongo-Config-1   : 192.168.16.42
  - Mongo-Config-2   : 192.168.16.43
  - Router           : 192.168.16.44
  - Mongo-Shard-1    : 192.168.16.45
  - Mongo-Shard-2    : 192.168.16.46
  - Mongo-Shard-3    : 192.168.16.47

## Konfigurasi Server
1. Membuat seluruh skrip sesuai dengan data tertera
2. Menginisiasi seluruh server menggunakan perintah
> Vagrant Up

## Konfigurasi MongoDB

1. Konfigurasi replikas set
   - Masuk ke salah satu server config
   - masuk mongo, lalu masukan kode
   ```
   mongo mongo-config-1:27019
   ```
   - inti Replika
   ```
   rs.initiate( { _id: "configReplSet", configsvr: true, members: [ { _id: 0, host: "mongo-config-1:27019" }, { _id: 1, host: "mongo-config-2:27019" }] } )
   ```
2. Membuat Admin User
   - Gunakan database admin
   ``` 
   use admin 
   ```
   - Lalu create user
   ```
   db.createUser({user: "mongo-admin", pwd: "password", roles:[{role: "root", db: "admin"}]})
   ```
3. Menambah Shard
   - Masuk ke salah satu server shard
   - Lakukan Koneksi Kepada MongoDB Query Router
   ```
   mongo mongo-query-router:27017 -u mongo-admin -p --authenticationDatabase admin
   ```
   - Tambahkan shard
   ```
   sh.addShard( "mongo-shard-1:27017" )
   sh.addShard( "mongo-shard-2:27017" )
   sh.addShard( "mongo-shard-3:27017" )
   ```
4. Aktifkan Database dan Koleksi
   - Tetap dalam server shard aktif dan terhubung pada router
   - keitkan kdoe berikut.
   ```
   use news
   sh.enableSharding("ufo")
   db.ufoCollection.ensureIndex( { _id : "hashed" } )
   sh.shardCollection( "ufo.ufoCollection", { "_id" : "hashed" } )
   ```
   
## Import Dataset Dan Hasil
1. Import Dataset
   - Masuk ke server router
   - Jalankan Perintah berikut
   ```
   mongoimport --host 192.168.16.23 --port 27017 --db ufo --collection ufoCollection --file /vagrant/dataset/complete.csv --type csv --headerline
   ```
2. Hasil dari Import Data
   - Tetap pada server router
   - masuk ke mongoDB
   ```
   mongo router:27017 -u mongo-admin -p --authenticationDatabase admin
   ```
   - Cek Sharding
   ```
   db.ufoCollection.getShardDistribution()
   ```
   
   
## Aplikasi mongoDB menggunakan API

1. Create

2. Read

3. Update

4. Delete

5. Aggregation 1

6. Aggregation 2
   
