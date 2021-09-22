#!/usr/bin/env ruby
require 'openssl'


class Chall
    def initialize(size)
        @size = size
        @p = OpenSSL::BN.generate_prime(@size * 2, true)
        @e = 0x10001
        @key = OpenSSL::PKey::RSA.new
        @key.set_key(@p.to_i, @e, nil)
    end

    def save
        File.binwrite('flag_enc', @key.public_encrypt(File.binread('flag')))
    end

    def enlighten(torch)
        n = @p
        for _ in 1..torch
            k = rand(1..(1 << @size))
            e = rand(1..(1 << (@size / 4 * 3)))
            puts (n * k + e).to_s(16)
        end
    end
end

SIZE, TORCH = 1024, 50
chall = Chall.new(SIZE)
chall.enlighten(TORCH)
chall.save
