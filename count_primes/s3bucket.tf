resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name

  #   lifecycle {
  #     prevent_destroy = true # Comment this out if you want to be able to destroy the bucket
  #   }

}
