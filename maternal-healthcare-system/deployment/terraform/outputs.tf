output "instance_ip" {
  value = aws_instance.maternal_healthcare_instance.public_ip
}

output "redis_endpoint" {
  value = aws_elasticache_cluster.maternal_healthcare_redis.configuration_endpoint
}

output "firestore_database_url" {
  value = google_firestore_database.maternal_healthcare_firestore.database_url
}