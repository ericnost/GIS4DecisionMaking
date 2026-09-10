source "https://rubygems.org"

gem "jekyll", "~> 4.3"

# Theme
gem "just-the-docs"

# JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

gem "csv", "~> 3.3"

gem "bigdecimal", "~> 4.1"