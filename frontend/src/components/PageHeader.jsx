export default function PageHeader({ title, description }) {
  return (
    <div className="mb-6">
      <h1 className="font-display text-xl font-semibold tracking-tight">
        {title}
      </h1>
      {description && (
        <p className="text-dim text-[13.5px] mt-1">{description}</p>
      )}
    </div>
  );
}
