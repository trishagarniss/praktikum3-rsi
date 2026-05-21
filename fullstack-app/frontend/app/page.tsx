import { AuthButtons } from "@/components/auth-buttons"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export default function Home() {
  return (
    <main className="flex flex-1 flex-col">
      <section className="flex flex-1 flex-col items-center justify-center gap-6 px-4 py-20">
        <h1 className="text-4xl font-bold tracking-tight">
          Selamat Datang di Acara RSI
        </h1>
        <p className="max-w-md text-center text-muted-foreground">
          Kelola pendaftaran acara dengan mudah, cepat, dan terorganisir
        </p>
        <AuthButtons />
      </section>

      <section className="border-t px-4 py-12">
        <div className="mx-auto grid max-w-5xl gap-6 md:grid-cols-3">
          <Card>
            <CardHeader>
              <CardTitle>Pendaftaran Mudah</CardTitle>
              <CardDescription>
                Daftar acara dalam hitungan menit
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Cukup isi data diri, pilih acara, dan kamu terdaftar secara otomatis.
              </p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Pantau Acara</CardTitle>
              <CardDescription>
                Lihat jadwal dan kuota tersedia
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Pantau semua acara yang tersedia beserta kuota peserta secara real-time.
              </p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Notifikasi</CardTitle>
              <CardDescription>
                Tetap terupdate
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-muted-foreground">
                Dapatkan informasi terbaru tentang acara yang kamu ikuti.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>
    </main>
  )
}
