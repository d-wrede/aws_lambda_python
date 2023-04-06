# resource "aws_s3_bucket_notification" "bucket_notification" {
#   bucket = aws_s3_bucket.bucket.id

#   topic {
#     topic_arn     = aws_sns_topic.sns_topic.arn
#     events        = ["s3:ObjectCreated:*"]
#     filter_suffix = ".log"
#   }
# }

# resource "aws_sns_topic" "sns_topic" {
#   name   = "prime-notification"
#   policy = data.aws_iam_policy_document.topic.json
# }

# resource "aws_sns_topic_subscription" "sns_subscription" {
#   topic_arn = aws_sns_topic.sns_topic.arn
#   protocol  = "email"
#   endpoint  = "daniel.wrede@posteo.de"
# }


# data "aws_iam_policy_document" "topic" {
#   statement {
#     effect = "Allow"

#     principals {
#       type        = "Service"
#       identifiers = ["s3.amazonaws.com"]
#     }

#     actions   = ["SNS:Publish"]
#     resources = ["arn:aws:sns:*:*:s3-event-notification-topic"]

#     condition {
#       test     = "ArnLike"
#       variable = "aws:SourceArn"
#       values   = [aws_s3_bucket.bucket.arn]
#     }
#   }
# }
